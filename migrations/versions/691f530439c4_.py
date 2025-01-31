"""empty message

Revision ID: 691f530439c4
Revises: 
Create Date: 2022-03-20 20:24:33.595302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '691f530439c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('bedroom', sa.String(length=80), nullable=True),
    sa.Column('bathroom', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('propertyType', sa.String(length=80), nullable=True),
    sa.Column('photo_name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Properties')
    # ### end Alembic commands ###
